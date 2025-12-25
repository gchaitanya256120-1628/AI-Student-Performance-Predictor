#include <stdio.h>

int main() {
    FILE *fp;
    int attendance, study_hours, internal_marks, result;

    fp = fopen("student_data.csv", "a");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    printf("Enter attendance (0-100): ");
    scanf("%d", &attendance);

    printf("Enter study hours per day: ");
    scanf("%d", &study_hours);

    printf("Enter internal marks (0-100): ");
    scanf("%d", &internal_marks);

    printf("Enter result (1 = Pass, 0 = Fail): ");
    scanf("%d", &result);

    fprintf(fp, "%d,%d,%d,%d\n", attendance, study_hours, internal_marks, result);

    fclose(fp);

    printf("Data saved successfully!\n");
    return 0;
}
