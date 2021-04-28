import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import pandas as pd
import os
from datetime import datetime
import cv2

from object_detection_image import run_object_detection_image
from object_detection_video import run_object_detection_video


def main():
    
    st.title('Object Detection')
    # 사이드바 메뉴
    menu = ['Home','Object Detection_image','Object Detection_video']
    choice = st.sidebar.selectbox("Menu",menu)

    if choice =='Home':
        st.write('이 앱은 스트림릿과 연동하여 물체 인식하는 앱입니다.')
        st.write('왼쪽의 사이드바에서 선택하세요.')

    elif choice == 'Object Detection_image' :
        run_object_detection_image()    

    elif choice == 'Object Detection_video' :
        run_object_detection_video()

if __name__ == '__main__':
    main()