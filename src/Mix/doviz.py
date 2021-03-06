# Veriler doviz.com adresinden alınmaktadır.
import re
from requests import get
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko"}

KEY1 = "Alış / Satış"
KEY2 = "Günlük Aralık"


def doviz(base_link):
    data = get(base_link, headers=headers)
    veri = data.content.decode("utf-8")
    # veri = veri[veri.find(KEY1 if KEY1 in veri else KEY2, 0):]

    a_s = []
    for key, desc in [(f'data-socket-attr="b">[\n\t\v ]*(.*)[\n\t\v ]*</', "Alış"),
                      (f'data-socket-attr="s">[\n\t\v ]*(.*)[\n\t\v ]*</', "Satış"),
                      (f'ay-2">Son (.*)<', "Son Güncelleme")
                      ]:
        x = re.search(key, veri)
        x = x and x.groups() and x.groups()[0]
        a_s.append(f"{desc}: {x.strip()}" if x else "")

    return a_s


class DovizExtension(Extension):
    def __init__(self):
        super(DovizExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []

        for i in range(7):
            x = extension.preferences["dov" + str(i)].split(";")
            if len(x) < 2:
                continue
            # Adres
            metin = doviz(x[1].strip())

            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name="{:10}{:20}{}".format(x[0].strip(), metin[0], metin[1]),
                description=metin[2],
                on_enter=OpenUrlAction(x[1] and x[1].strip()))
            )

        return RenderResultListAction(items)


if __name__ == '__main__':
    DovizExtension().run()