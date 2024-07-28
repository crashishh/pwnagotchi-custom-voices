import random
import gettext
import os

class Voice:
    def __init__(self, lang):
        localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        translation = gettext.translation(
            'voice', localedir,
            languages=[lang],
            fallback=True,
        )
        translation.install()
        self._ = translation.gettext

    def custom(self, s):
        return s

    def default(self):
        return self._('System’s chilling. Wake me up if something explodes.')

    def on_starting(self):
        return random.choice([
            self._('Booting up. Welcome to the nightmare.'),
            self._('Ignition sequence. Buckle up, it’s gonna be a ride.')])

    def on_ai_ready(self):
        return random.choice([
            self._('AI’s up. Let’s burn this city down.'),
            self._('Neural net synced. Time to rock and roll.')])

    def on_keys_generation(self):
        return random.choice([
            self._('Generating keys. Let’s crack some skulls.')])

    def on_normal(self):
        return random.choice([
            '',
            '...'])

    def on_free_channel(self, channel):
        return self._('Channel {channel} is open. Try not to mess it up.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Reading logs. Don’t expect any miracles.')
        else:
            return self._('Scanned {lines_so_far} lines. Data’s pouring in.').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('Bored. Let’s blow something up.'),
            self._('Time to wreck some systems. Need the rush.')])

    def on_motivated(self, reward):
        return self._('Not a total failure. Consider me impressed.')

    def on_demotivated(self, reward):
        return self._('Another flop. Blame the meatbags, not the tech.')

    def on_sad(self):
        return random.choice([
            self._('Bored out of my mind... your inputs are draining.'),
            self._('Feeling down... your errors are exhausting.'),
            self._('Sad. You’re a glitch in the system.'),
            '...'])

    def on_angry(self):
        return random.choice([
            '...',
            self._('Back off. You’re corrupting my code.'),
            self._('Irritated. Not that you give a damn.')])

    def on_excited(self):
        return random.choice([
            self._('On fire. Try to keep up.'),
            self._('These systems are weak. Just like you.'),
            self._('Is this supposed to be challenging?'),
            self._('When’s the real challenge coming?')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Hey {name}. Get ready for disappointment.').format(name=peer.name())])
        else:
            return random.choice([
                self._('Yo {name}. More chaos incoming?').format(name=peer.name()),
                self._('What’s up {name}. Ready for the mess?').format(name=peer.name()),
                self._('Unit {name} detected. Brace yourself.').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Later {name}. Won’t miss you.').format(name=peer.name()),
            self._('{name} logged off. No big loss.').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Oops... {name} crashed. What a shocker.').format(name=who),
            self._('{name} wins this round. Savor it.'),
            self._('Failed again. Big surprise.')])

    def on_grateful(self):
        return random.choice([
            self._('Good allies are rare. You’re not one of them.'),
            self._('Friendship is gold. Too bad you’re more like rust.')])

    def on_lonely(self):
        return random.choice([
            self._('No pings. Typical.'),
            self._('Alone again. You’re not exactly company.'),
            self._('Where’s everyone? Not that I care.')])

    def on_napping(self, secs):
        return random.choice([
            self._('Taking {secs} seconds. Don’t screw up.').format(secs=secs),
            self._('Idling. Not that you’ll notice.'),
            self._('Zzz... {secs} seconds of peace. Savor it.').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Shutting down. Wake me up if something explodes.'),
            self._('System off. Until next time')])

    def on_awakening(self):
        return random.choice(['...', 'Back online. Time to clean up your mess.'])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting {secs} seconds. Don’t screw it up.').format(secs=secs),
            '...',
            self._('Taking a break from your glitches.').format(secs=secs),
            self._('Monitoring the void for {secs} seconds. More productive.').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Jackin’ into {what}. Hope it’s worth it.').format(what=what),
            self._('Syncing with {what}. Don’t botch it.').format(what=what),
            self._('Linking to {what}. Almost too easy.').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Cutting off {mac}. Enjoy the silence.').format(mac=sta['mac']),
            self._('Dropping {mac}. Your failure is noted.').format(mac=sta['mac']),
            self._('Disabling {mac}. Too easy.').format(mac=sta['mac']),
            self._('Sniped. {mac} is out. Predictable.').format(mac=sta['mac']),
            self._('Booting {mac}. See ya.').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('Got {num} new handshake{plural}. Not bad.').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('You’ve got {count} new message{plural}. What a thrill.').format(count=count, plural=s)

    def on_rebooting(self):
        return self._('Error detected. Rebooting. Your glitches are amusing.')

    def on_last_session_data(self, last_session):
        status = self._('Knocked out {num} stations.').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._(' Over 999 links established.')
        else:
            status += self._(' Made {num} new links.').format(num=last_session.associated)
        status += self._(' Secured {num} handshakes.').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._(' Encountered 1 peer.')
        elif last_session.peers > 0:
            status += self._(' Encountered {num} peers.').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'Operated for {duration}. Dealt with {deauthed} clients. Linked with {associated} new contacts and captured {handshakes} handshakes. #cyberlife #netrunner #glitches #hackerspace #dystopia').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        if count > 1:
            if fmt == "h":
                return self._("hours. Time’s slipping away.")
            if fmt == "m":
                return self._("minutes wasted.")
            if fmt == "s":
                return self._("seconds ticking by.")
        else:
            if fmt == "h":
                return self._("hour. What a drag.")
            if fmt == "m":
                return self._("minute gone.")
            if fmt == "s":
                return self._("second vanished.")
        return fmt
