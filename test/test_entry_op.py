# coding:utf-8

import tempfile
import unittest
import os

from entry_op import EntryOp

import config
import logging


class TestEntryOp(unittest.TestCase):
    """
    EntryOp class in entry_op.py
    """

    def setUp(self):
        self.ext = "txt"
        self.tempdir = tempfile.gettempdir()
        self.tempfile = os.path.join(self.tempdir, "tmp." + self.ext)

        with open(self.tempfile, "wb") as f:
            f.write(b"Delete me!")

        dir_name = "tmpDir"
        self.create_dir_path = os.path.join(self.tempdir, dir_name)

    def test_dir_exsit(self):
        self.assertTrue(EntryOp.dir_exsist(self.tempdir))

    def test_dir_create(self):
        EntryOp.dir_create(self.create_dir_path)
        self.assertTrue(EntryOp.dir_exsist(self.create_dir_path))

        os.removedirs(self.create_dir_path)  # test用のため作成したデイレクトリは削除しておく

    def test_file_exist(self):
        logging.debug(f"{self.tempfile}を見つけました")
        self.assertTrue(EntryOp.file_exist(self.tempfile))

    def test_file_list_no_ext(self):
        flist = EntryOp.file_list(self.tempdir)
        logging.debug(f"{len(flist)}個が見つかりました")
        self.assertGreaterEqual(len(flist), 1)

    def test_file_list_txt_ext(self):
        flist = EntryOp.file_list(self.tempdir, "txt")
        logging.debug(f"{len(flist)}個が見つかりました")
        self.assertGreaterEqual(len(flist), 1)

    def tearDown(self):
        os.remove(self.tempfile)


if __name__ == "__main__":
    unittest.main()
