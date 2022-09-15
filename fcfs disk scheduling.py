size = int(input("enter the size"))
def FCFS(arr, head):
	seek_count = 0;
	distance, cur_track = 0, 0;
	for i in range(size):
		cur_track = arr[i];
		distance = abs(cur_track - head);
		seek_count += distance;
		head = cur_track;
	print("Total number of seek operations = ",seek_count);
	print("Seek Sequence is");
	for i in range(size):
		print(arr[i]);
if _name_ == '_main_':
	arr = list(map(int,input().strip().split()))
	head = int(input("enter the head position"))
	FCFS(arr, head);
