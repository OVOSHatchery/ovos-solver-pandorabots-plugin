import all_the_chatbots
from ovos_plugin_manager.templates.solvers import QuestionSolver


class PandoraBotsSolver(QuestionSolver):
    enable_tx = True
    priority = 97
    bots = all_the_chatbots.bot_map()

    def __init__(self, config=None):
        super().__init__(config)
        self.default_bot = self.config.get("bot", "professor")

    # officially exported Solver methods
    def get_spoken_answer(self, query, context=None):
        context = context or {}
        bot_name = context.get("bot") or self.default_bot
        if bot_name in self.bots:
            return self.bots[bot_name](query)
        for bot in self.bots.values():
            try:
                return bot(query)
            except:
                continue


if __name__ == "__main__":
    bot = PandoraBotsSolver()
    print(bot.get_spoken_answer("hello!"))
    print(bot.spoken_answer("Qual é a tua comida favorita?", {"lang": "pt-pt"}))
