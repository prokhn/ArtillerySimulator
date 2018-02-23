import time

class Logger:
    def __init__(self, ok='✔', warn='⚠', error='✘', type_sep=': ', time_need=False, immed_write=True, to_conlose=True, outfile='log.txt'):
        self.type_ok = ok
        self.type_warn = warn
        self.type_error = error
        self.type_sep = type_sep
        self.time_need = time_need
        self.immed_write = immed_write
        self.to_console = to_conlose
        self.outfile = outfile

        self.time_start = time.time()

        self.messages = []
        self.messages.append('Game starting time - %s' % time.asctime())

    def save(self):
        with open(self.outfile, 'w', encoding='utf-8') as file:
            file.write(self.messages[0] + '\n')
            file.write('=' * 50 + '\n')
            for msg in self.messages[1:]:
                file.write(msg + '\n')
            file.write('Saving time - %s\n' % time.asctime())
            file.write('=' * 50 + '\n')
            file.write('Program runs %s sec' % str(round(time.time() - self.time_start, 2)))

    def __call__(self, ms_type, message, console_only=False):
        if self.time_need:
            crtime = time.strftime('%H:%M:%S')
        else:
            crtime = time.strftime('%H:%M:%S')

        if ms_type == 'o':
            tp = self.type_ok
        elif ms_type == 'w':
            tp = self.type_warn
        elif ms_type == 'e':
            tp = self.type_warn
        else:
            tp = '!!(Unknown type)!!'

        msg = tp + '(%s)' % crtime + self.type_sep + message
        if not console_only:
            self.messages.append(msg)

        if self.to_console:
            print('Logger: %s' % msg)

        if self.immed_write:
            self.save()
