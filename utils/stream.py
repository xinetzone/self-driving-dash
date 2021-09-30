from pathlib import Path
import tables
import pandas as pd


class Stream:
    def __init__(self, path):
        self.path = path
        self.frame_id_list = self._frame_id_list()
        self.frame_dict = {k:frame_id for k, frame_id in enumerate(self.frame_id_list)}

    def _frame_id_list(self):
        if not Path(self.path).exists():
            frame_id_list = []
        else:
            with tables.open_file(self.path) as h:
                frame_id_list = [int(str(frame).split(' ')[0].replace('/frame_', ''))
                                 for frame in h.iter_nodes('/')]
            frame_id_list.sort()
        return frame_id_list

    def __len__(self):
        return len(self.frame_id_list)

    def to_pandas(self, frame_id):
        frame_id = self.frame_dict[frame_id]
        return pd.read_hdf(self.path, f'frame_{frame_id}')

    def __getitem__(self, frame_id):
        if len(self) == 0:
            h = 'null'
        else:
            if frame_id in self.frame_id_list:
                h = self.to_pandas(frame_id)
            elif isinstance(frame_id, slice):
                h = [self.to_pandas(ID)
                     for ID in range(*frame_id.indices(len(self)))]
                h = pd.concat(h)
            else:
                h = 'unreal'
        return h

    @property
    def min_id(self):
        if len(self) == 0:
            return 0
        else:
            return min(self.frame_id_list)

    @property
    def max_id(self):
        if len(self) == 0:
            return 0
        else:
            return len(self)
    
    @property
    def marks(self):
        if len(self) == 0:
            return {0: '0'}
        else:
            return {
                k: '' # frame_id
                for k, frame_id in self.frame_dict.items()
            }