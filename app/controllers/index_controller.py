from flask import render_template
#don't change this import or it can't find the module controller
from  . controller import ControllerBase


class IndexController(ControllerBase):
    @staticmethod
    def get():
        name = "Thomas Kim"
        return render_template('../simple_pages/templates/index.html', name=name)
