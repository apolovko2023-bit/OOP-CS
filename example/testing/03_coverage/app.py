
class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @property
    def get_angles(self):
        if self.shape_type == "triangle":
            return 60, 60, 60
        elif self.shape_type == "square":
            return 90, 90, 90, 90
        elif self.shape_type == "rectangle":
            return 90, 90, 90, 90
        else:
            raise ValueError("Невідомий тип фігури")


def main():
    shape = Shape("triangle")
    print(shape.get_angles)


if __name__ == "__main__":  # pragma: no cover
    main()

