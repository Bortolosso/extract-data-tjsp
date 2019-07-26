#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

from dotted_dict import DottedDict

class Constants:

    def __init__(self):

        self.WORKING_DIR = "/opt/robot/robotorios"

        self.CAC_SCP = DottedDict({
            "SP": {
                "URL": "https://www.tjsp.jus.br/cac/scp/webmenupesquisa.aspx"
            }
        })
