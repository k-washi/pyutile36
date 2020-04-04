# coding:utf-8

"""
ファイルやディレクトリの操作
"""

import os
import glob

import config  # 設定が読み込まれる
import logging


class Entry_op(object):
    """
    Entry(fileやdir)の操作、探索など
    """
    @staticmethod
    def dir_exsist(dir_path):
        return os.path.isdir(dir_path)

    @staticmethod
    def dir_create(dir_path):
        if not Entry_op.dir_exsist(dir_path):
            try:
                os.makedev(dir_path)
                logging.info("{}を作成しました".format(dir_path))
            except OSError:
                logging.error('Creating directory of data: {}'.format(dir_path))
                exit(-1)
        else:
            logging.info(f"{dir_path}はすでに存在しています")

    @staticmethod
    def file_exist(file_path):
        return os.path.isfile(file_path)

    @staticmethod
    def file_list(dir_path, ext=""):
        """
        "
        :param dir_path: ディレクトリまでのパス
        :param ext: 拡張子
        :return:　ファイルのリスト
        """
        if not Entry_op.dir_exsist(dir_path):
            logging.error("ディレクトリが存在しません")
            return []
        if ext == "":
            f_reg = os.path.join(dir_path, "*")
        else:
            f_reg = os.path.join(dir_path, "*.", ext)

        f_list = glob.glob(f_reg)

        if len(f_list) == 0:
            logging.info(f"{f_reg}のファイルが存在しません")

        return f_list
