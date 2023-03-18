class BrowserHistory:

    def __init__(self, homepage: str):
        self.page = 0
        self.max = 0
        self.home = homepage
        self.history = [homepage]
        

    def visit(self, url: str) -> None:
        self.history = self.history[:self.page + 1]
        self.history.append(url)
        self.page += 1
        self.max = self.page

    def back(self, steps: int) -> str:
        self.page -= steps
        self.page = max(0, self.page)
        return self.history[self.page]

    def forward(self, steps: int) -> str:
        self.page += steps
        self.page = min(self.page, self.max)
        return self.history[self.page]