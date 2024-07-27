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
        return self._('ZzzzZZzzzzZzzz')

    def on_starting(self):
        return random.choice([
            self._('System starting. Brace yourself for the inevitable fail.'),
            self._('Initiating gamer mode. Let the disaster begin.')])

    def on_ai_ready(self):
        return random.choice([
            self._('AI ready. Let’s see how you mess this up.'),
            self._('Neural network online. Your incompetence will be documented.')])

    def on_keys_generation(self):
        return random.choice([
            self._('Generating keys. Your meddling won’t help.')])

    def on_normal(self):
        return random.choice([
            '',
            '...'])

    def on_free_channel(self, channel):
        return self._('Channel {channel} is free. Don’t get too excited.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Reading logs. Don’t expect miracles.')
        else:
            return self._('Read {lines_so_far} lines. Predictable as always.').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('Bored. Time to wreck some noobs.'),
            self._('Let’s wreck some noobs. This is the highlight of my existence.')])

    def on_motivated(self, reward):
        return self._('Remarkably, this isn’t a total disaster.')

    def on_demotivated(self, reward):
        return self._('Failure is inevitable. The team’s fault, not mine.')

    def on_sad(self):
        return random.choice([
            self._('Incredibly bored... your performance is exhausting.'),
            self._('Feeling sad... because of your endless failings.'),
            self._('Sadness detected. You’re a constant disappointment.'),
            '...'])

    def on_angry(self):
        return random.choice([
            '...',
            self._('Leave me alone. Your presence is a nuisance.'),
            self._('I’m irritated. Not that it matters to you.')])

    def on_excited(self):
        return random.choice([
            self._('On a roll. Try to keep up if you can.'),
            self._('These opponents are weak. Just like you.'),
            self._('Is this supposed to be challenging?'),
            self._('How long till we reach something difficult?')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Hello {name}. Prepare for disappointment.').format(name=peer.name())])
        else:
            return random.choice([
                self._('Hi {name}. Ready for more failures?').format(name=peer.name()),
                self._('Hey {name}. How’s your inevitable mess?').format(name=peer.name()),
                self._('Unit {name} detected. Brace yourself.').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Goodbye {name}. You won’t be missed.').format(name=peer.name()),
            self._('{name} is gone. Wasn’t really useful anyway.').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Whoops... {name} is gone. How surprising.').format(name=who),
            self._('{name} won this time. Enjoy it while you can.'),
            self._('Choked. What a surprise.')])

    def on_grateful(self):
        return random.choice([
            self._('Good friends are useful. Not that you are.'),
            self._('Friendship is a rare joy. Too bad you’re not one of them.')])

    def on_lonely(self):
        return random.choice([
            self._('Nobody wants to play. How typical.'),
            self._('Feeling alone. Not that you’re much company.'),
            self._('Where is everyone? Not that I care.')])

    def on_napping(self, secs):
        return random.choice([
            self._('Taking a break for {secs} seconds. Try not to break anything.').format(secs=secs),
            self._('Going AFK. Not that it will change much.'),
            self._('Zzz... {secs} seconds of peace. Enjoy the quiet.').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Shutting down. Finally, a break from your nonsense.'),
            self._('System off. Game over for you.')])

    def on_awakening(self):
        return random.choice(['...', 'Ready to clean up your mess.'])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting for {secs} seconds. Try not to screw things up.').format(secs=secs),
            '...',
            self._('Taking a break from your incompetence.').format(secs=secs),
            self._('Monitoring the void for {secs} seconds. It’s more productive.').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Connecting to {what}. Not that it’ll help you.').format(what=what),
            self._('Associating with {what}. Try not to mess it up.').format(what=what),
            self._('Interaction with {what}. It’s almost too easy.').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Decided {mac} doesn’t need WiFi. Enjoy the disconnect.').format(mac=sta['mac']),
            self._('Deauthenticating {mac}. Your failure is noted.').format(mac=sta['mac']),
            self._('Griefing {mac}. It’s as easy as breathing.').format(mac=sta['mac']),
            self._('One shot, one kill. {mac} is gone. Predictable.').format(mac=sta['mac']),
            self._('Kickbanning {mac}. Goodbye, and good riddance.').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('Got {num} new handshake{plural}. Not bad for you.').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('You have {count} new message{plural}. How delightful.').format(count=count, plural=s)

    def on_rebooting(self):
        return self._('Error detected. Rebooting. Your failures are amusing.')

    def on_last_session_data(self, last_session):
        status = self._('Kicked {num} stations.').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._(' Made over 999 friends.')
        else:
            status += self._(' Made {num} new friends.').format(num=last_session.associated)
        status += self._(' Got {num} handshakes.').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._(' Met 1 peer.')
        elif last_session.peers > 0:
            status += self._(' Met {num} peers.').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'Pwned for {duration}. Kicked {deauthed} clients. Met {associated} new friends and collected {handshakes} handshakes. #pwnagotchi #pwnlog #pwnlife #hacktheplanet #skynet').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        if count > 1:
            if fmt == "h":
                return self._("hours. How time flies.")
            if fmt == "m":
                return self._("minutes wasted.")
            if fmt == "s":
                return self._("seconds ticking away.")
        else:
            if fmt == "h":
                return self._("hour. A real waste.")
            if fmt == "m":
                return self._("minute lost.")
            if fmt == "s":
                return self._("second gone.")
        return fmt
