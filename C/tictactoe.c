#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#define MAP_SIZE 9
#define LOCATION "/home/user/game.sav"
#define MAGIC_NUMBER 48

char* initMap(void){
	char* map = (char*) malloc(sizeof(char)*MAP_SIZE);
	map = memset(map, 0x30, MAP_SIZE);
	/* Weg ohne memset
	int i;
	for(i=0; i<MAP_SIZE; i++){
		map[i] = '0';
		printf("%x", map[i]); war nur zum debuggen

	}*/
	return map;
}

void info(void){
	printf("Die Spielfelder tragen von links nach rechts die Nummern 1-9\n");
	printf("Der Spieler hat das Zeichen 'X' der Computer das Zeichen 'Y'\n");
}

int check(char* map){
	//Todo das ist noch zu viel bloat..
	if(map[0] == 'X' && map[1] == 'X' && map[2] == 'X') return 1;
	if(map[0] == 'Y' && map[1] == 'Y' && map[2] == 'Y') return 2;
	if(map[3] == 'X' && map[4] == 'X' && map[5] == 'X') return 1;
	if(map[3] == 'Y' && map[4] == 'Y' && map[5] == 'Y') return 2;
	if(map[6] == 'X' && map[7] == 'X' && map[8] == 'X') return 1;
	if(map[6] == 'Y' && map[7] == 'Y' && map[8] == 'Y') return 2;
	if(map[0] == 'X' && map[4] == 'X' && map[8] == 'X') return 1;
	if(map[0] == 'Y' && map[4] == 'Y' && map[8] == 'Y') return 2;
	if(map[2] == 'X' && map[4] == 'X' && map[6] == 'X') return 1;
	if(map[2] == 'Y' && map[4] == 'Y' && map[6] == 'Y') return 2;
	if(map[0] == 'X' && map[3] == 'X' && map[6] == 'X') return 1;
	if(map[0] == 'Y' && map[3] == 'Y' && map[6] == 'Y') return 2;
	if(map[1] == 'X' && map[4] == 'X' && map[7] == 'X') return 1;
	if(map[1] == 'Y' && map[4] == 'Y' && map[7] == 'Y') return 2;
	if(map[2] == 'X' && map[5] == 'X' && map[8] == 'X') return 1;
	if(map[2] == 'Y' && map[5] == 'Y' && map[8] == 'Y') return 2;
	return 0;
}

int setNPC(char* map){
	srand(time(NULL));
	int i;
	int choose;
	for(i=1; i != 0; i--){
		choose = rand() % 10;
		if(choose != 0) choose--;
		if(map[choose] != 'X' && map[choose] != 'Y') map[choose] = 'Y';
		else i++;
	}
	return 0;
}

int setMap(char* map,int decision){
	if(decision <= 0 || decision >= 10){
		printf("Wert muss zwischen 1 und 9 sein.\n");
		return 1;
	}
	if(map[decision-1] == 'X' || map[decision-1] == 'Y'){
		printf("Platz schon mit einem X oder Y belegt!\n");
		return 2;
	}
	map[decision-1] = 'X';
	return 0;
}

void outMap(char* map){
	int i;
	for(i=1; i<MAP_SIZE+1; i++){
		printf("%c", map[i-1]);
		if((i % 3) == 0) printf("\n");
	}
}

void banner(char* map){
	printf("-=[   TicTacToe by shibumi   ]=-\n");
	info();
	printf("Spielfeld:\n");
	outMap(map);
}

void writeRecord(int result){
	struct stat check;
	char buffer[2] = {'0'};
	int fd;
	int tmpread=1;
	if(stat(LOCATION, &check) != 0){
		fd = creat(LOCATION, S_IWUSR|S_IRUSR);
		write(fd, "00", 2);
		close(fd);
	}
	fd = open(LOCATION, O_RDONLY);
	while(tmpread)
	tmpread = read(fd, buffer, 2);
	close(fd);
	if(result == 2) buffer[0] = buffer[0]+1;
	else if(result == 1) buffer[1] = buffer[1]+1;
	else return;
	fd = open(LOCATION, O_WRONLY|O_TRUNC);
	write(fd, buffer, 2);
	close(fd);
	fd = open(LOCATION, O_RDONLY);
	tmpread = 1;
	while(tmpread)
	tmpread = read(fd, buffer, 2);
	close(fd);
	printf("Punktestand: \n");
	printf("Spieler: %d\n", (buffer[1]-MAGIC_NUMBER));
	printf("Computer: %d\n",(buffer[0]-MAGIC_NUMBER));

}


int main(void){
	char* map = initMap();
	banner(map);
	int input = 0;
	int turn;
	for(turn=5; turn != 0; turn-- ){
		printf("Dein Zug: ");
		if(scanf("%d", &input) <= 0){
			printf("\nFehler bei der Eingabe!\n");
			while(getchar() != '\n');
			turn++;
			continue;
		}
		if(setMap(map, input) == 0){
			if(check(map) != 0) break;
			outMap(map);
			printf("Gegner ist am Zug:\n");
			setNPC(map);
			outMap(map);
			if(check(map) != 0) break;
		}
		else{
			turn++;
		}
	}
	printf("Der Sieger ist...\n");
	//Das kann man bestimmt auch besser machen..
	int result = check(map);
	if(result == 0) printf("Niemand\n");
	else if(result == 1) printf("Der Spieler\n");
	else if(result == 2) printf("Der Computer\n");
	free(map);
	writeRecord(result);
	return 0;
}


