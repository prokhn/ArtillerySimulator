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

        self.messages = []

    def save(self):
        if len(self.messages) == 0:
            with open(self.outfile, 'w', encoding='utf-8') as file:
                file.write('No logs')
        elif len(self.messages) == 1:
            with open(self.outfile, 'w', encoding='utf-8') as file:
                file.write(self.messages[0])
        else:
            with open(self.outfile, 'w', encoding='utf-8') as file:
                for msg in self.messages[:-1]:
                    file.write(msg + '\n')
                file.write(self.messages[-1])

    def __call__(self, ms_type, message, console_only=False):
        if self.time_need:
            # TODO time converting
            crtime = ''
        else:
            crtime = ''

        if ms_type == 'o':
            tp = self.type_ok
        elif ms_type == 'w':
            tp = self.type_warn
        elif ms_type == 'e':
            tp = self.type_warn
        else:
            tp = '!!(Unknown type)!!'

        msg = tp + self.type_sep + message
        if not console_only:
            self.messages.append(msg)

        if self.to_console:
            print('Logger: %s' % msg)

        if self.immed_write:
            self.save()
