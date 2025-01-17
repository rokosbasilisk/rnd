{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import nle\n",
    "import gym \n",
    "import random\n",
    "import numpy as np\n",
    "from PIL import Image, ImageDraw\n",
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "env = gym.make(\"NetHackChallenge-v0\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "obs = env.reset()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'glyphs': array([[2359, 2359, 2359, ..., 2359, 2359, 2359],\n",
       "        [2359, 2359, 2359, ..., 2359, 2359, 2359],\n",
       "        [2359, 2359, 2359, ..., 2359, 2359, 2359],\n",
       "        ...,\n",
       "        [2359, 2359, 2359, ..., 2359, 2359, 2359],\n",
       "        [2359, 2359, 2359, ..., 2359, 2359, 2359],\n",
       "        [2359, 2359, 2359, ..., 2359, 2359, 2359]], dtype=int16),\n",
       " 'chars': array([[32, 32, 32, ..., 32, 32, 32],\n",
       "        [32, 32, 32, ..., 32, 32, 32],\n",
       "        [32, 32, 32, ..., 32, 32, 32],\n",
       "        ...,\n",
       "        [32, 32, 32, ..., 32, 32, 32],\n",
       "        [32, 32, 32, ..., 32, 32, 32],\n",
       "        [32, 32, 32, ..., 32, 32, 32]], dtype=uint8),\n",
       " 'colors': array([[0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0]], dtype=uint8),\n",
       " 'specials': array([[0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0]], dtype=uint8),\n",
       " 'blstats': array([28,  9, 17, 17, 14, 18,  9,  8,  9,  0, 16, 16,  1,  0,  2,  2,  8,\n",
       "         0,  1,  0,  1,  1,  0,  0,  1,  0]),\n",
       " 'message': array([ 72, 101, 108, 108, 111,  32,  65, 103, 101, 110, 116,  44,  32,\n",
       "        119, 101, 108,  99, 111, 109, 101,  32, 116, 111,  32,  78, 101,\n",
       "        116,  72,  97,  99, 107,  33,  32,  32,  89, 111, 117,  32,  97,\n",
       "        114, 101,  32,  97,  32, 110, 101, 117, 116, 114,  97, 108,  32,\n",
       "        104, 117, 109,  97, 110,  32,  67,  97, 118, 101, 109,  97, 110,\n",
       "         46,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0], dtype=uint8),\n",
       " 'inv_glyphs': array([1965, 1975, 2351, 2352, 2019, 5976, 5976, 5976, 5976, 5976, 5976,\n",
       "        5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976,\n",
       "        5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976,\n",
       "        5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976,\n",
       "        5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976],\n",
       "       dtype=int16),\n",
       " 'inv_strs': array([[97, 32, 43, ...,  0,  0,  0],\n",
       "        [97, 32, 43, ...,  0,  0,  0],\n",
       "        [49, 52, 32, ...,  0,  0,  0],\n",
       "        ...,\n",
       "        [ 0,  0,  0, ...,  0,  0,  0],\n",
       "        [ 0,  0,  0, ...,  0,  0,  0],\n",
       "        [ 0,  0,  0, ...,  0,  0,  0]], dtype=uint8),\n",
       " 'inv_letters': array([ 97,  98,  99, 100, 101,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0], dtype=uint8),\n",
       " 'inv_oclasses': array([ 2,  2, 13, 13,  3, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18,\n",
       "        18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18,\n",
       "        18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18,\n",
       "        18, 18, 18, 18], dtype=uint8),\n",
       " 'tty_chars': array([[ 72, 101, 108, ...,  32,  32,  32],\n",
       "        [ 32,  32,  32, ...,  32,  32,  32],\n",
       "        [ 32,  32,  32, ...,  32,  32,  32],\n",
       "        ...,\n",
       "        [ 32,  32,  32, ...,  32,  32,  32],\n",
       "        [ 65, 103, 101, ...,  32,  32,  32],\n",
       "        [ 68, 108, 118, ...,  32,  32,  32]], dtype=uint8),\n",
       " 'tty_colors': array([[7, 7, 7, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [7, 7, 7, ..., 0, 0, 0],\n",
       "        [7, 7, 7, ..., 0, 0, 0]], dtype=int8),\n",
       " 'tty_cursor': array([10, 28], dtype=uint8),\n",
       " 'misc': array([0, 0, 0], dtype=int32)}"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 67,  97, 118, ...,  32,  32,  32],\n",
       "       [ 32,  32,  32, ...,  32,  32,  32],\n",
       "       [ 32,  32,  32, ...,  32,  32,  32],\n",
       "       ...,\n",
       "       [ 32,  32,  32, ...,  32,  32,  32],\n",
       "       [ 65, 103, 101, ...,  32,  32,  32],\n",
       "       [ 68, 108, 118, ...,  32,  32,  32]], dtype=uint8)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obs['tty_chars']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "random_action = random.randint(0,113)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "q = env.step(random_action)[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'glyphs': array([[2359, 2359, 2359, ..., 2359, 2359, 2359],\n",
       "        [2359, 2359, 2359, ..., 2359, 2359, 2359],\n",
       "        [2359, 2359, 2359, ..., 2359, 2359, 2359],\n",
       "        ...,\n",
       "        [2359, 2359, 2359, ..., 2359, 2359, 2359],\n",
       "        [2359, 2359, 2359, ..., 2359, 2359, 2359],\n",
       "        [2359, 2359, 2359, ..., 2359, 2359, 2359]], dtype=int16),\n",
       " 'chars': array([[32, 32, 32, ..., 32, 32, 32],\n",
       "        [32, 32, 32, ..., 32, 32, 32],\n",
       "        [32, 32, 32, ..., 32, 32, 32],\n",
       "        ...,\n",
       "        [32, 32, 32, ..., 32, 32, 32],\n",
       "        [32, 32, 32, ..., 32, 32, 32],\n",
       "        [32, 32, 32, ..., 32, 32, 32]], dtype=uint8),\n",
       " 'colors': array([[0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0]], dtype=uint8),\n",
       " 'specials': array([[0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0]], dtype=uint8),\n",
       " 'blstats': array([28,  9, 17, 17, 14, 18,  9,  8,  9,  0, 16, 16,  1,  0,  2,  2,  8,\n",
       "         0,  1,  0,  1,  1,  0,  0,  1,  0]),\n",
       " 'message': array([ 67,  97, 118, 101, 109, 101, 110,  32,  97, 114, 101, 110,  39,\n",
       "        116,  32,  97,  98, 108, 101,  32, 116, 111,  32, 117, 115, 101,\n",
       "         32, 116, 119, 111,  32, 119, 101,  97, 112, 111, 110, 115,  32,\n",
       "         97, 116,  32, 111, 110,  99, 101,  46,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0], dtype=uint8),\n",
       " 'inv_glyphs': array([1965, 1975, 2351, 2352, 2019, 5976, 5976, 5976, 5976, 5976, 5976,\n",
       "        5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976,\n",
       "        5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976,\n",
       "        5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976,\n",
       "        5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976, 5976],\n",
       "       dtype=int16),\n",
       " 'inv_strs': array([[97, 32, 43, ...,  0,  0,  0],\n",
       "        [97, 32, 43, ...,  0,  0,  0],\n",
       "        [49, 52, 32, ...,  0,  0,  0],\n",
       "        ...,\n",
       "        [ 0,  0,  0, ...,  0,  0,  0],\n",
       "        [ 0,  0,  0, ...,  0,  0,  0],\n",
       "        [ 0,  0,  0, ...,  0,  0,  0]], dtype=uint8),\n",
       " 'inv_letters': array([ 97,  98,  99, 100, 101,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0], dtype=uint8),\n",
       " 'inv_oclasses': array([ 2,  2, 13, 13,  3, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18,\n",
       "        18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18,\n",
       "        18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18,\n",
       "        18, 18, 18, 18], dtype=uint8),\n",
       " 'tty_chars': array([[ 67,  97, 118, ...,  32,  32,  32],\n",
       "        [ 32,  32,  32, ...,  32,  32,  32],\n",
       "        [ 32,  32,  32, ...,  32,  32,  32],\n",
       "        ...,\n",
       "        [ 32,  32,  32, ...,  32,  32,  32],\n",
       "        [ 65, 103, 101, ...,  32,  32,  32],\n",
       "        [ 68, 108, 118, ...,  32,  32,  32]], dtype=uint8),\n",
       " 'tty_colors': array([[7, 7, 7, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0, ..., 0, 0, 0],\n",
       "        [7, 7, 7, ..., 0, 0, 0],\n",
       "        [7, 7, 7, ..., 0, 0, 0]], dtype=int8),\n",
       " 'tty_cursor': array([10, 28], dtype=uint8),\n",
       " 'misc': array([0, 0, 0], dtype=int32)}"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "q"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = nle.nethack.tty_render(q['tty_chars'], q['tty_colors'], q['tty_cursor'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [],
   "source": [
    "def process_frame(frame):\n",
    "    blstats = frame['blstats']\n",
    "    msg = frame['message']\n",
    "    message = ''\n",
    "    for c in msg:\n",
    "        message = message+chr(c)\n",
    "    img = nle.nethack.tty_render(frame['tty_chars'],frame['tty_colors'],frame['tty_cursor'])\n",
    "    ansi_escape = re.compile(r'\\x1B(?:[@-Z\\\\-_]|\\[[0-?]*[ -/]*[@-~])')\n",
    "    img = ansi_escape.sub('', img).split('\\n')[2:-2]\n",
    "    frame = ''\n",
    "    for l in img:\n",
    "        frame = frame+l+'\\n'\n",
    "    img = Image.new(mode='RGB',size=(790,370))\n",
    "    text = ImageDraw.Draw(img)\n",
    "    text.text((0, 0),frame, fill=(255,255,255))\n",
    "    return np.array(img),message.split('\\x00')[0],blstats"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x7febd2119510>"
      ]
     },
     "execution_count": 194,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "imshow(process_frame(q)[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
