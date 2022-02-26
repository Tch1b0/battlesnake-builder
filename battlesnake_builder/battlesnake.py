from typing import Callable, Literal
from flask import Flask, request
from battlesnake_builder.reqdata import Data


class Config():
    apiversion: str
    author:      str
    color:       str
    head:        str
    tail:        str
    version:     str

    def __init__(
        self,
        apiversion: str = "1",
        author:      str = "Unknown",
        color:       str = "#ffffff",
        head:        str = "default",
        tail:        str = "default",
        version:     str = "1"
    ) -> None:
        self.apiversion = apiversion
        self.author = author
        self.color = color
        self.head = head
        self.tail = tail
        self.version = version

    @classmethod
    def from_json(cls, json: dict):
        return cls(
            json["apiversion"],
            json["author"],
            json["color"],
            json["head"],
            json["tail"],
            json["version"]
        )

    def to_json(self) -> dict:
        return {
            "apiversion": self.apiversion,
            "author": self.author,
            "color": self.color,
            "head": self.head,
            "tail": self.tail,
            "version": self.version
        }


class BattleSnake():
    server: Flask = Flask(__name__)
    config: Config
    config_callback: Callable[[None], Config | dict] = None
    start_callback:  Callable[[Data], None] = None
    turn_callback:   Callable[[Data],
                              Literal["up", "right", "left", "down"]] = None
    end_callback:    Callable[[Data], None] = None

    def __init__(self, config: Config | dict = None) -> None:
        if config is not None:
            if type(config) is dict:
                tmp = Config().to_json()
                tmp.update(config)
                self.config = Config.from_json(tmp)
            else:
                self.config = config
        else:
            self.config = Config()

    def on_config(self, callback: Callable[[], Config | dict]) -> None:
        self.config_callback = callback

    def on_start(
            self, callback: Callable[[Data], None]):
        self.start_callback = callback

    def on_move(
            self, callback: Callable[[Data], Literal["up", "right", "left", "down"]]):
        self.turn_callback = callback

    def on_end(self, callback: Callable[[Data], None]):
        self.end_callback = callback

    def server_get_config(self):
        if self.config_callback is None:
            return self.config.to_json()

        value = self.config_callback()
        if type(value) is Config:
            value = Config.to_json()

        default_config = self.config.to_json()
        default_config.update(value)

        return default_config

    def server_post_start(self):
        if self.start_callback is not None:
            self.start_callback(Data.from_json(request.get_json()))
        return "Ok"

    def server_post_move(self):
        return "up" if self.turn_callback is None else self.turn_callback(Data.from_json(request.get_json()))

    def server_post_end(self):
        if self.end_callback is not None:
            self.end_callback(Data.from_json(request.get_json()))
        return "Ok"

    def run(self, host: str = "localhost", port: int = 3000):
        self.server.add_url_rule(
            "/", "server_get_config", self.server_get_config)
        self.server.add_url_rule(
            "/start", "server_post_start", self.server_post_start, methods=["POST"])
        self.server.add_url_rule(
            "/move", "server_post_move", self.server_post_move, methods=["POST"])
        self.server.add_url_rule(
            "/end", "server_post_end", self.server_post_end, methods=["POST"])

        self.server.run(host=host, port=port)
