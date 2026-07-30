from core.store import Store


def before_scenario(context, scenario):
    context.store = Store()
    context.output = ""
