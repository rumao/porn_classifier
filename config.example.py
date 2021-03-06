
class Config():

    def __init__(self):

        self.ROOT_DIR = '../'  # 專案的root
        self.DATA_DIR = self.ROOT_DIR + 'data/'
        self.TRAIN_DATA_DIR = self.DATA_DIR + 'train_coarse/'
        self.MODELBASE_DIR = self.ROOT_DIR + 'programs/model_base/'  # 儲存trained model的目錄
        self.LOG_DIR = self.ROOT_DIR + 'programs/logs/'  # 儲存log的目錄

        self.SEED = 18035
        self.TEST_DATA_RATIO = 0.1

        self.EPOCHS = 50
        self.VAL_RATIO = 0.2  # validatino data的比例，其餘為training
        self.BATCH_SIZE = 32
        self.LEARNING_RATE = 1e-3

        self.IMG_SIZE = (299, 299)
        # self.CLASS_NUM = 3

        # 隱藏層的設定(neuron數, activation func)，越靠後越靠近輸出層
        self.DENSE_INFOS = [
            (1024, 'relu'),
            # (1024, 'relu'),
        ]

        import logging
        self.LOG_LEVEL = logging.DEBUG

        self.STAGE_INFOS = {
            'porn': {
                # 'classes': ['1-normal', 'sensity'],
                'classes': ['normal', 'sensity'],
                'model_id': 'init_stage_porn_classifier.20190622151509.val_loss.02-0.3213-0.8876',
            },
            'fine_porn': {
                # 'classes': ['2-bikini', 'all_naked'],
                'classes': ['bikini', 'naked'],
                'model_id': 'soft_porn_classifier.20190622035912.05-0.3722',
            }
        }


    def __repr__(self):

        VAR_PER_LINE = 3
        repr_lines, repr_strs = [], []
        for key, value in self.__dict__.items():
            repr_strs.append('\'%s\': %s'%(key,value))
            if len(repr_strs)>(VAR_PER_LINE-1):
                repr_lines.append(', '.join(repr_strs))
                repr_strs = []
        if len(repr_strs)>0:
            repr_lines.append(', '.join(repr_strs))

        return '\n'.join(repr_lines)


CONFIG = Config()

if __name__ == '__main__':
    
    print('config: \n%s'%CONFIG)