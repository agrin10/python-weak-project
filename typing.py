from time import time


def typeerror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors =errors +1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1]==words[i+1]) & (inwords[i-1]==words[i - 1]):
                   continue
                else:
                    errors +=1
            else:
                errors +=1
    return errors

# calculating speed of typing words per minute

def speed(inprompt, stime,etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords= len(inwords)
    speed = twords / time

    return speed

#calculating the total time

def elapsedtime(stime,etime):
    time =etime - stime  # etime==end time   stime == start time
    return time


if __name__ =="__main__":
    prompt = "\n\nPython is a high-level, general-purpose programming language. \nIts design philosophy emphasizes code readability with the use of significant indentation\n .Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.\nPython is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported,\n and many of their features support functional programming and aspect-oriented programming (including metaprogramming and metaobjects).\n Many other paradigms are supported via extensions, including design by contract and logic programming.\n\n"
    # pragraph we type 
    print(f"type this:- '{prompt}'")

    
input('press enter when your ready to check your speed!!!')

# recording time 
stime = time()
inprompt =input()
etime =time()

# collecting information returned by function

time = round(elapsedtime(stime, etime), 2)
speed = speed(inprompt , stime , etime)
errors = typeerror(prompt)

print(f'total time elapsed: {time} secondes')
print(f"your averang typing speed was {speed} words per minute (w/m)")
print(f"with {errors} errors")



