import cv2, time

first_frame = None
video = cv2.VideoCapture(0)
print(video.isOpened()) 

if video.isOpened():
    while True:
        check, frame = video.read()  
        if frame != None:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            if first_frame is None:
                first_frame = gray
                continue
            
            delta_frame = cv2.absdiff(first_frame, gray)
            thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
            
            (_, cnts, _) = cv2.findContours(thresh_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            for contour in cnts:
                if cv2.contourArea(contour) < 1000:
                    continue
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
                
            
            cv2.imshow("Gray Frame", gray)
            cv2.imshow("Delta Frame", delta_frame)
            cv2.imshow("Threshold Frame", thresh_frame)
            cv2.imshow("Color Frame", frame)
            
            key = cv2.waitKey(50)
            
            if key == ord("q"):
                break
        else:
            print("Frame not available")
            print(video.isOpened()) 

    
    video.release()
    cv2.destroyAllWindows()    
else:
    print("Got an error because of cam")
    
