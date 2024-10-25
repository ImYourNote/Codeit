class Node:
    def __init__(self, station):
        self.station = station
        self.next = None

class howToGo:
    def __init__(self):
        self.head = None

    def append(self, station):
        if self.isStationIn(station):
            print(f"{station}역은 이미 입력된 경로입니다.")
            return
        
        new_node = Node(station)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def isStationIn(self, station):
        current = self.head
        while current:
            if current.station == station:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        route = []

        while current:
            route.append(current.station)
            current = current.next

        return " -> ".join(route)

    def reverse_display(self):
        current = self.head
        stack = []

        while current:
            stack.append(current.station)
            current = current.next

        reverse_route = []
        while stack:
            reverse_route.append(stack.pop())

        return " -> ".join(reverse_route)

if __name__ == "__main__":
    route = howToGo()

    while True:
        station = input("추가할 지하철역 이름을 입력하세요 (종료하려면 0 입력): ")

        if station == '0':
            print("프로그램을 종료합니다.")
            break

        route.append(station)

        print("\n---------현재 경로---------")

        homeToSchool = route.display()
        if homeToSchool:
            print("1. 집에서 학교까지:", homeToSchool)
        
        schoolToHome = route.reverse_display()
        if schoolToHome:
            print("2. 학교에서 집까지:", schoolToHome)
