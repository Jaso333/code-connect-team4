import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';
import { MatTableModule } from '@angular/material/table';
import { MatToolbarModule } from '@angular/material/toolbar';
import { UserFormComponent, UserData } from '../user-form/user-form.component';

const USER_DATA: UserData[] = [
  {
    id: 1,
    username: 'johndoe',
    name: 'John Doe',
    bio: 'Software developer with 10 years of experience.',
    githubProfileUrl: 'https://github.com/johndoe',
    skills: 'JavaScript, TypeScript, Angular',
    profileImageUrl: 'https://example.com/johndoe.jpg',
    createdAt: new Date('2022-01-01'),
    updatedAt: new Date('2023-01-01')
  },
  {
    id: 2,
    username: 'janedoe',
    name: 'Jane Doe',
    bio: 'Frontend developer and UI/UX designer.',
    githubProfileUrl: 'https://github.com/janedoe',
    skills: 'HTML, CSS, Angular, Figma',
    profileImageUrl: 'https://example.com/janedoe.jpg',
    createdAt: new Date('2022-02-01'),
    updatedAt: new Date('2023-02-01')
  },
  {
    id: 3,
    username: 'samsmith',
    name: 'Sam Smith',
    bio: 'Full stack developer with a passion for open source.',
    githubProfileUrl: 'https://github.com/samsmith',
    skills: 'Node.js, Express, Angular, MongoDB',
    profileImageUrl: 'https://example.com/samsmith.jpg',
    createdAt: new Date('2022-03-01'),
    updatedAt: new Date('2023-03-01')
  }
];

@Component({
  selector: 'app-user-table',
  standalone: true,
  imports: [MatTableModule, CommonModule, MatToolbarModule, MatButtonModule, MatIconModule, MatDialogModule],
  templateUrl: './user-table.component.html',
  styleUrls: ['./user-table.component.css']
})
export class UserTableComponent {
  displayedColumns: string[] = ['id', 'username', 'name', 'bio', 'githubProfileUrl', 'skills', 'profileImageUrl', 'createdAt', 'updatedAt', 'actions'];
  dataSource = USER_DATA;

  constructor(public dialog: MatDialog) { }

  public addUser(userData: UserData | null = null): void {
    const dialogRef = this.dialog.open(UserFormComponent, {
      data: userData
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        // Handle the result from the form submission
        console.log('User added:', result);
      }
    });
  }

  public editUser(userData: UserData): void {
    this.addUser(userData);
  }
}
