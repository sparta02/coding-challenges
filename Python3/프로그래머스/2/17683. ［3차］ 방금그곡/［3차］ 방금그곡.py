def solution(m, musicinfos):
    m=m.replace('C#', 'K')
    m=m.replace('D#', 'L')
    m=m.replace('F#', 'I')
    m=m.replace('G#', 'M')
    m=m.replace('A#', 'N')
    print(m)
    answer = ''
    candidates=[]
    for i in range(len(musicinfos)):
        start, end, name, song=musicinfos[i].split(',')
        song=song.replace('C#', 'K')
        song=song.replace('D#', 'L')
        song=song.replace('F#', 'I')
        song=song.replace('G#', 'M')
        song=song.replace('A#', 'N')
        time=(int(end[:2])-int(start[:2]))*60+(int(end[3:])-int(start[3:]))
        text=song*(time//(len(song)))+song[:time%(len(song))]
        if m in text:
            candidates.append((time, i, name))
    
    candidates.sort(key=lambda x:(-x[0], x[1]))
    if not candidates:
        return "(None)"
    return candidates[0][2]
