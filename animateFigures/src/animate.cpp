#define PICS "./pics/"
#include "animate.h"

//current picture position
int currPic;
//directory with picture files in it
ofDirectory dir(PICS);
//pause toggle
bool pauseAnimation;
//for Image list
int maxImages = 20;
ofImage images[20];
//animation speed
int currSpeed = 1;
int maxSpeed = 60;
int minSpeed = 1;



//--------------------------------------------------------------
void ofApp::setup(){
    //populate directory
    dir.listDir();
    
    //sets initial framerate
    ofSetFrameRate(currSpeed);
    
    //animation should run at start
    pauseAnimation = false;
    
    currPic = -1;

    int temp = maxImages;
    
    if (dir.numFiles() < maxImages){
        temp = dir.numFiles();
    }
    
    
    for (unsigned i = 0; i < temp; i++){
        images[i].loadImage(dir.getPath(i));
        images[i].resize(ofGetWindowWidth()-100, ofGetWindowHeight()-100);
    }
    
}

//--------------------------------------------------------------
void ofApp::update(){
    
    //sets the current speed of the animations
    ofSetFrameRate(currSpeed);
    
    //sets the current picture to the next (or first) picture;
    if (!pauseAnimation){
        currPic++;
        if (currPic >= dir.numFiles()) {
            currPic = 0;
        }
    }

}

//--------------------------------------------------------------
void ofApp::draw(){
    //draws the current picture
    images[currPic].draw(50, 50);
    
    
    //for debug reasons the current framerate
    ofDrawBitmapString(ofToString(ofGetFrameRate()) + " fps", 10, 15);

}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    if (key == ' ') {
        if (pauseAnimation){
            pauseAnimation = false;
        } else {
            pauseAnimation = true;
        }
    }
    if (key == '=' && currSpeed <= maxSpeed) {
        currSpeed++;
    }
    if (key == '-' && currSpeed >= minSpeed) {
        currSpeed--;
    }
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}
