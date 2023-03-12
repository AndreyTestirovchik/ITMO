from task_9_checks import Checks


class Input(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


search = Input('ввод', 'loc#search')
ok = Input('ок', 'loc#ok')
back = Input('esc', 'loc#back')
enter = Input('принять', 'loc#enter')


search.check_text()
ok.check_text()
back.check_text()
enter.check_text()


class Button(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


button_1 = Button('кнопка_1', 'loc#button_1')
button_2 = Button('кнопка_2', 'loc#button_2')
button_3 = Button('кнопка_3', 'loc#button_3')
button_4 = Button('кнопка_4', 'loc#button_4')

button_1.check_text()
button_2.check_text()
button_3.check_text()
button_4.check_text()


class Title(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


title_1 = Title('тайтл_1', 'loc#тайтл_1')
title_2 = Title('тайтл_2', 'loc#тайтл_2')
title_3 = Title('тайтл_3', 'loc#тайтл_3')
title_4 = Title('тайтл_4', 'loc#тайтл_4')

title_1.check_text()
title_2.check_text()
title_3.check_text()
title_4.check_text()


class Link(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


link_1 = Link('ссылка_1', 'loc#url_1')
link_2 = Link('ссылка_2', 'loc#url_2')
link_3 = Link('ссылка_3', 'loc#url_3')
link_4 = Link('ссылка_4', 'loc#url_4')

link_1.check_text()
link_2.check_text()
link_3.check_text()
link_4.check_text()
