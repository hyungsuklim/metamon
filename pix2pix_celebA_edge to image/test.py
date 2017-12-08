import argparse
import os
import scipy.misc
import numpy as np

from model import pix2pix
import tensorflow as tf

parser = argparse.ArgumentParser(description='')
parser.add_argument('--dataset_name', dest='dataset_name', default='train_data', help='name of the dataset(celeba or facades)')
parser.add_argument('--epoch', dest='epoch', type=int, default=200, help='# of epoch')
parser.add_argument('--batch_size', dest='batch_size', type=int, default=1, help='# images in batch')
parser.add_argument('--train_size', dest='train_size', type=int, default=1e8, help='# images used to train')
parser.add_argument('--load_size', dest='load_size', type=int, default=286, help='scale images to this size')
parser.add_argument('--fine_size', dest='fine_size', type=int, default=256, help='then crop to this size')
parser.add_argument('--ngf', dest='ngf', type=int, default=64, help='# of gen filters in first conv layer')
parser.add_argument('--ndf', dest='ndf', type=int, default=64, help='# of discri filters in first conv layer')
parser.add_argument('--input_nc', dest='input_nc', type=int, default=3, help='# of input image channels')
parser.add_argument('--output_nc', dest='output_nc', type=int, default=3, help='# of output image channels')
parser.add_argument('--niter', dest='niter', type=int, default=200, help='# of iter at starting learning rate')
parser.add_argument('--lr', dest='lr', type=float, default=0.0002, help='initial learning rate for adam')
parser.add_argument('--beta1', dest='beta1', type=float, default=0.5, help='momentum term of adam')
parser.add_argument('--flip', dest='flip', type=bool, default=True, help='if flip the images for data argumentation')
parser.add_argument('--which_direction', dest='which_direction', default='AtoB', help='AtoB or BtoA')
parser.add_argument('--phase', dest='phase', default='train', help='train, test')
parser.add_argument('--save_epoch_freq', dest='save_epoch_freq', type=int, default=50, help='save a model every save_epoch_freq epochs (does not overwrite previously saved models)')
parser.add_argument('--save_latest_freq', dest='save_latest_freq', type=int, default=5000, help='save the latest model every latest_freq sgd iterations (overwrites the previous latest model)')
parser.add_argument('--print_freq', dest='print_freq', type=int, default=50, help='print the debug information every print_freq iterations')
parser.add_argument('--continue_train', dest='continue_train', type=bool, default=False, help='if continue training, load the latest model: 1: true, 0: false')
parser.add_argument('--serial_batches', dest='serial_batches', type=bool, default=False, help='f 1, takes images in order to make batches, otherwise takes them randomly')
parser.add_argument('--serial_batch_iter', dest='serial_batch_iter', type=bool, default=True, help='iter into serial image list')
parser.add_argument('--checkpoint_dir', dest='checkpoint_dir', default='./checkpoints_1', help='models are saved here')
parser.add_argument('--sample_dir', dest='sample_dir', default='./sample', help='sample are saved here')
parser.add_argument('--test_dir', dest='test_dir', default='./test', help='test sample are saved here')
parser.add_argument('--L1_lambda', dest='L1_lambda', type=float, default=100.0, help='weight on L1 term in objective')

args = parser.parse_args()

PATH = './checkpoints_1/train_data_1_256/pix2pix.model-576502'
test_dir = './datasets/train_data/test/'
save_dir = './datasets/train_data/result/'

def test(self,args):
    init_op = tf.global_variables_initializer()
    self.sess.run(init_op)

    sample_files = glob('./datasets/{}/test/*.jpg'.format(self.dataset_name))

    n = [int(i) for i in map(lambda x: x.split('/')[-1].split('.jpg')[0],sample_files)]
    sample_files = [x for (y,x) in sorted(zip(n,sample_files))]

    print("Loading testing images ...")
    sample = [load_data(sample_files, is_test=True) for sample_file in sample_files]

    if(self.is_grayscale) :
        sample_images = np.array(sample).astype(np.float32)[:,:,:,None]
    else :
        sample_images = np.array(sample).astype(np.float32)

    sample_images = [sample_images[i:i+self.batch_size]
                     for i in xrange(0,len(sample_images), self.batch_size)]
    sample_images = np.array(sample_images)
    print(sample_images.shape)

    start_time = time.time()
    if self.load(self.checkpoint_dir):
        print(" [*] Load SUCCESS")
    else :
        print(" [!] Load failed...")

    for i,sample_image in enumerate(sample_images) :
        idx = i + 1
        print("sampling image ",idx)
        samples = self.sess.run(
            self.fake_B_sample,
            feed_dict={self.real_data: sample_image}
        )
        samples = tf.concat([samples, self.real_A], 6)
        save_images(sampels, [self.batch_size, 1],
                    './{}/test_{:04d}.png'.format(args.test_dir, idx))


def main(_):
    if not os.path.exists(args.checkpoint_dir):
        os.makedirs(args.checkpoint_dir)
    if not os.path.exists(args.sample_dir):
        os.makedirs(args.sample_dir)
    if not os.path.exists(args.test_dir):
        os.makedirs(args.test_dir)

    with tf.Session() as sess:
        model = pix2pix(sess, image_size=args.fine_size, batch_size=args.batch_size,
                        output_size=args.fine_size, dataset_name=args.dataset_name,
                        checkpoint_dir=args.checkpoint_dir, sample_dir=args.sample_dir)

        if args.phase == 'train':
            model.train(args)
        else:
            model.test(args)

if __name__ == '__main__':
    tf.app.run()
