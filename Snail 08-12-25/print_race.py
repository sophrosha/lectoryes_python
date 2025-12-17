import time

def print_race(snails):
    print("\n" + "=" * 55)
    for snail in snails:
        display_name = (snail.name[:10] if len(snail.name) <= 10 else snail.name[:9] + ".")
        display_name = display_name.ljust(10)
        track = '-' * snail.position + '@' + '-' * (40 - snail.position)
        status = ""
        if snail.finished:
            status = " (FINISH)"
        elif snail.is_drifting:
            status = " (DRIFT!)"
        elif snail.is_sleeping:
            status = " (Zzz...)"
        print(f"{display_name}: {track}{status}")
    print("=" * 55)
    time.sleep(0.5)