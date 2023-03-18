import json

def readJSON(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data
def hand_dominance(json_path):
    data = readJSON(json_path)
    dominant_hand = data.get("dominantHand", None)
    drawn_hand = data.get("drawnHand", None)

    if (dominant_hand == "right" and drawn_hand == "right") or\
            (dominant_hand == "left" and drawn_hand == "left"):
        return "dominant"
    elif (dominant_hand == "right" and drawn_hand == "left") or\
            (dominant_hand == "left" and drawn_hand == "right"):
        return "non-dominant"
    else:
        return "ambidextrous"
