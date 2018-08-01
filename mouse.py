import pygame, sys


class Observer:
    def __init__(self, subject):
        self.subject = subject
        self.subject.add_observer(self)

    def on_notify(self):
        pass

class Artist(Observer):

    def on_notify(self, event):
        if event == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            print(pygame.mouse.get_cursor())

class Mouse:

    def __init__(self):
        self.observers = set()
        self.num_obs = len(self.observers)
        self.notifications = set()

    def add_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        self.observers.discard(observer)

    def add_notification(self, notification):
        self.notifications.add(notification)

    def notify(self):
        for notification in self.notifications:
            for obs in self.observers:
                obs.on_notify(notification)
        self.notifications = set()


class Main:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.wieght, self.height = 512, 512

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self.running = True
        self.mouse = Mouse()
        Artist(self.mouse)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse.add_notification(pygame.MOUSEBUTTONDOWN)

    def on_loop(self):
        self.mouse.notify()

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = Main()
    theApp.on_execute()
