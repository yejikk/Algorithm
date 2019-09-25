def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    while bridge:
        time += 1
        bridge.pop(0)

        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time

solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])