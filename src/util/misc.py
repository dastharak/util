class spinner:

    characters = ('|','/','-','\\')

    def __init__(self):
        self.print_turning_pipe = 0
        pass

    def printtp(self):
        print(spinner.characters[self.print_turning_pipe],end='',flush=True)
        self.print_turning_pipe=(self.print_turning_pipe+1)%4
        print('\b\r',end='',flush=True)
