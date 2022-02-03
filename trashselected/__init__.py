from fman import DirectoryPaneCommand, show_alert
import os
from fman.url import as_human_readable
from fman.url import as_url


class trashselected(DirectoryPaneCommand):
    def __call__(self):
        selected_files = self.pane.get_selected_files()
        output = ""
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            for i in range(len(selected_files)):
                os.system(f"trash '{selected_files[i].replace('file://', '')}'")


