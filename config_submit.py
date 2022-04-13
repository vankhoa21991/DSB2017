config = {'datapath':'/home/vankhoa@median.cad/datasets/MedDec/DataBowl3/stage2/',
          'preprocess_result_path':'prep_result/',
          'outputfile':'prediction.csv',
          
          'detector_model':'net_detector',
         'detector_param':'./model/detector.ckpt',
         'classifier_model':'net_classifier',
         'classifier_param':'./model/classifier.ckpt',
         'n_gpu':1,
         'n_worker_preprocessing':None,
         'use_exsiting_preprocessing':False,
         'skip_preprocessing':True,
         'skip_detect':True}
