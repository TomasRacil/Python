from GUI import eventHandler, updateSurface


def main():
    while True:
        if eventHandler() == 0:
            break
        updateSurface()


if __name__ == "__main__":
    main()
