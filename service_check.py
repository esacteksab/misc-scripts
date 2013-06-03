import time
from checks import AgentCheck
from hashlib import md5
import psutil


class SERVICECheck(AgentCheck):

    def check(self, instance):
        """
        from psutil.process_iter() checking to see if process exists
        if process exists, all is well in the world, if not, tell us
        """
        try:
            import psutil
        except ImportError:
            raise Exception('You need the "ps" package to run this check")

        if 'name' not in instance:
            raise KeyError('The "name" of the service is mandatory')
        name = instance.get('name', None)
        # A unique ID for aggregation of events
        aggregation_key = md5(name).hexdigest()
        processes = []
        iter_procs = psutil.process_iter()

        try:
            processes = [p.name for p in iter_procs if p.name == name]
        except psutil.AccessDenied, e:
            self.log.error('Access denied to %s process' % name)
            self.log.error('Error: %s' % e)
            raise

        if name not in processes:
            self._not_running(name, aggregation_key, instance)
            return

    def _not_running(self, name, aggregation_key, instance):
        """
        this posts an event to DataDog's dashboard
        if service == sshd
        if notify == hipchat-ops
        Message Title would be 'Service sshd NOT Running'
        Message Text would be 'sshd is not running @hipchat-ops should investigate'
        """
        notify = instance.get('notify', self.init_config.get('notify', []))
        print notify
        self.log.info(notify)
        notify_message = ""
        if notify:
            notify_list = []
            for handle in notify:
                # DataDog uses a Twitter-like notifier with prefixing contacts
                # with @ symbol -- we don't include such in your yaml file
                notify_list.append("@%s" % handle.strip())
                notify_message = " ".join(notify_list) + " \n"
        self.event({
            'timestamp': int(time.time()),
            'event_type': 'service_check',
            'msg_title': 'Service %s NOT Running' % name,
            'msg_text': '%s is not running %s should investigate' % (name,
                                                                     notify_message),
            'aggregation_key': aggregation_key
        })

if __name__ == '__main__':
    check, instances = SERVICECheck.from_yaml('/etc/dd-agent/conf.d/service_check.yaml')
    for instance in instances:
        print "\nRunning the check for service %s" % (instance['name'])
        check.check(instance)
        if check.has_events():
            print 'Events: %s' (check.get_events())
