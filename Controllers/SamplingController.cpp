#include <essentia.h>
#include <json/value.h>
#include <stdbool.h>
#include <vector>
//include json

class SamplingController
{
    public:

    int sampleTime,sampleRate,waitTime,offset;
    int* array;
    bool exit_flag, finished;

    /*
      mainThread
      model
      metadata
    */

    void SamplingController(int sampleTime=15, int sampleRate=48000, string waitTime)
    {
        this.sampleTime = sampleTime;
        this.sampleRate = sampleRate;

        if (waitTime.compare("") != 0)
        {
            this.waitTime = atoi(waitTime);
        }else
        {
            this.waitTime = 45;
        }

        //Include essentia related stuff here

        this.offset = 0;
        this.array = (int*)malloc(this.sampleRate*15*sizeof(int));
    }

    void mainSample()
    {
        this.exit_flag = false;
        while (!this.exit_flag)
        {
            this.finished = false;
            //INCLUDE THREAD CODE HERE
            bool workdone = false;
            while (!this.finished)
            {
                if(!this.offset == 14 && !workdone)
                {
                    this.performAnalysis();
                    workdone = true;
                }
            }
            this.finished = false;
            //INCLUDE THREAD CODE HERE
            while (!this.finished)
            {
                continue;
            }
        }
    }

    void appendAudio(string audioPath)
    {
        if (this.offset == 14)
        {
            this.offset = 0;
        }
        //ESSENTIA LOADER
        //std::vector<int> audio = essentia loader;
        IntegerVector idx = IntegerVector::create(this.offset*this.sampleRate, (this.offset+1)*this.sampleRate);
        //self.array[idx] = audio;
        this.offset++;
    }

    void timer(int timer)
    {
        //c++ threading sleep function here
        this.finished = true;
    }

    int getSampleTime()
    {
        return this.sampleTime;
    }

    int getWaitTime()
    {
        return this.waitTime;
    }

    void setSampleTime(int sampleTime)
    {
        this.sampleTime = sampleTime;
    }

    void setWaitTime(int waitTime)
    {
        this.waitTime = waitTime;
    }

    void performAnalysis()
    {
        //int scaled = this.array;

    }

    std::vector<string> parseTags(std::vector<double> activations)
    {
        std::vector<string> tags;
        int count = 0;
        for (int i = 0; i < this.metadata.length; i++)
        {
            double probability = activations[i];
            string label = this.metadata[i];
            if ((int) ((float) probability * 100) > 50)
            {
                tags.push_back(parseTag(label));
            }
        }
        return tags;
    }

    string parseTag(string label)
    {
        switch(label)
        {
            case "blu":
                return "Blues";
            case "cla":
                return "Classic";
            case "cou":
                return "Country";
            case "dis":
                return "Disco";
            case "hip":
                return "Hip Hop";
            case "jaz":
                return "Jazz";
            case "met":
                return "Metal";
            case "pop":
                return "Pop";
            case "reg":
                return "Reggae";
            case "roc":
                return "Rock";
        }
    }
};
