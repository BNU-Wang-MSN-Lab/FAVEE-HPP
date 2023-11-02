import pandas as pd
import numpy as np
import os
from transformers import pipeline
import torch

class HookManager:
    def __init__(self):
        self.hook_handles = []

    def add_hook(self, module, fn):
        hook_handle = module.register_forward_hook(fn)
        self.hook_handles.append(hook_handle)
        return True

    def remove_hooks(self):
        for v in self.hook_handles:
            v.remove()
        self.hook_handles = []
        return True


class utils(object):
    def __init__(self, arr: list, tokenizer) -> None:
        self.arr_tit = arr
        self.tokenizer = tokenizer

    def write(self, msg, name="", reset=False):
        path = "bert_embedding_data"
        if not os.path.exists(path):
            os.mkdir(path)

        with open(
            "./{}/{}.csv".format(path, name), "w" if reset else "a", encoding="utf-8"
        ) as f:
            f.write(msg)
        return True

    def get_Pos(self, sentence: str) -> list:
        arr = []  # result
        if len(sentence) == 0:
            return arr
        # return [-5, -4]
        r = self.tokenizer(sentence)
        r.reverse()
        for v in self.arr_tit:
            if v == "CLS":
                arr.append(0)
            elif v == "MASK":
                i = r.index("[MASK]") + 2
                arr.append(-i)
            else:
                i = r.index(v) + 2
                arr.append(-i)
        # print(arr)
        return arr

    """
    @param :name: 层名称
    @param :word: 词内容
    """
    def getHook(self, name, word="temp", sentence="", reset=False):
        if reset:
            for i in self.arr_tit:
                title = "{}_{}".format(i, name)
                self.write("", title, True)
                self.write("word,", title)
                self.write(",".join(["{}".format(x) for x in range(768)]), title)
                self.write("\n", title)

        tokenPosition = self.get_Pos(sentence)

        def hook_m(module, input, output):
            # [0, 2, -4, -3] [CLS, relationship, mask1, mask2
            tensor_data = None
            if name == "embedding_output":
                tensor_data = output.last_hidden_state
            else:
                tensor_data = output[0]
            tensor_data = tensor_data[0, tokenPosition, :].to("cpu")

            for i in range(len(self.arr_tit)):
                title = "{}_{}".format(self.arr_tit[i], name)
                self.write(f"{word},", title)
                self.write(",".join([f"{j}" for j in tensor_data[i, :]]), title)
                self.write("\n", title)
        return hook_m

if __name__ == "__main__":
    device = torch.device("cuda:0")
    hook_manager = HookManager()
    unmasker = pipeline("feature-extraction", model="bert-large-uncased", device=device)