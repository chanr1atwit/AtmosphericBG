#include <essentia\src\essentia\algorithmfactory.h>
#include <essentia\src\essentia\essentiamath.h>
#include <vector>
#include <iostream>
#include <string>
#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif
//include json

using namespace std;
using namespace essentia;
using namespace essentia::standard;

class SamplingControllerCPP
{
    public:


    essentia::init();
    Algorithm* model;
    

    SamplingControllerCPP() //st = sampleTime, sr = sampleRate, wt = waitTime, ap = audioPath
    {
        
        model = factory.create("TensorflowPredictMusiCNN", "graphFilename", "Files/genre_tzanetakis-musicnn-msd-1.pb");
    }

    vector<double> performAnalysis(string audiofile)
    {
        // Factory for loader
        AlgorithmFactory& factory = standard::AlgorithmFactory::instance();
        // Create loader from factory
        Algorithm* audio = factory.create("MonoLoader", "filename", audiofile, "sampleRate", this->sampleRate);
        vector<Real> audioBuffer;
        audio->output("audio").set(audioBuffer);
        vector<double> activations = this->model(audio);
        return activations;
    }
};

extern "C" {
    SamplingControllerCPP* SamplingControllerCPP_new() { return new SamplingControllerCPP(); }
    void SamplingControllerCPP_performAnalysis(SamplingControllerCPP* samplingControllerCPP) { samplingControllerCPP->performAnalysis(audiofile); }
}