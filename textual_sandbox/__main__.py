import sys
import logging
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Tree, Static, Button, Header


class TreeApp(App):
    CSS_PATH = "horizontal_layout.tcss"

    def compose(self) -> ComposeResult:
        yield Header(id="header")

        tree: Tree[dict] = Tree("Dune")
        tree.root.expand()
        characters = tree.root.add("Characters", expand=True)
        characters.add_leaf("Paul")
        characters.add_leaf("Jessica")
        characters.add_leaf("Chani")
        yield tree

        yield Static(renderable="", classes="box", id="mybox")
        #yield Button("Yes", id="yes", variant="primary")
        #yield Static("Two", classes="box")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        logging.info("On button pressed")

    def on_tree_node_highlighted(self, event: Tree.NodeSelected) -> None:
        mybox: Static = self.query_one("#mybox")
        if not event.node.allow_expand:
            mybox.update("leaf")
        else:
            mybox.update("node")


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d | %(levelname)s | %(module)s.%(funcName)s | %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    app = TreeApp()
    app.run()


if __name__ == "__main__":
    main()
