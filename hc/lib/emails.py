from django.conf import settings
from djmail.template_mail import InlineCSSTemplateMail


def _ctx(ctx):
    _ctx = {"host": settings.HOST}
    _ctx.update(ctx)
    return _ctx


def login(to, ctx):
    o = InlineCSSTemplateMail("login")
    o.send(to, _ctx(ctx))


def set_password(to, ctx):
    o = InlineCSSTemplateMail("set-password")
    o.send(to, _ctx(ctx))


def alert(to, ctx):
    o = InlineCSSTemplateMail("alert")
    o.send(to, _ctx(ctx))


def verify_email(to, ctx):
    o = InlineCSSTemplateMail("verify-email")
    o.send(to, _ctx(ctx))


def report(to, ctx):
    o = InlineCSSTemplateMail("report")
    o.send(to, _ctx(ctx))
