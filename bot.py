from chatbot import Chat, register_call
import translators as ts
import wikipedia


@register_call("whoIs")
def who_is(session, query):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "Maaf Saya masih belum tahu apa yang anda tanyakan :("


def ask(text):
    textEn = ts.google(text, from_language="id", to_language="en")

    res = Chat("pattern.template").say(textEn)

    res = ts.google(res, from_language="en", to_language="id",
                    if_ignore_limit_of_length=True)

    return res