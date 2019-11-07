def berlin_clock_time(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))

    single_seconds = seconds_row_lights(seconds % 2)
    five_hours = row_lights(
        light_colour="R",
        lights_on=hours // 5,
        lights_in_row=4)
    single_hours = row_lights(
        light_colour="R",
        lights_on=hours % 5,
        lights_in_row=4)
    five_minutes = row_lights(
        light_colour="Y",
        lights_on=minutes // 5,
        lights_in_row=11)
    single_minutes = row_lights(
        light_colour="Y",
        lights_on=minutes % 5,
        lights_in_row=4)

    return [
        single_seconds,
        five_hours,
        single_hours,
        five_minutes,
        single_minutes
    ]


def seconds_row_lights(seconds):
    return ["Y","O"][seconds%2]


def row_lights(
        light_colour,
        lights_on,
        lights_in_row):
    return light_colour * lights_on + "O" * (lights_in_row - lights_on)


if __name__ == "__main__":
    time = input()
    result = berlin_clock_time(time)
    print ("\n".join(result))


