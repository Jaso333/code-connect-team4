import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';
import { MatTableModule } from '@angular/material/table';
import { MatToolbarModule } from '@angular/material/toolbar';
import { UserFormComponent, UserData } from '../user-form/user-form.component';
import { UsersService } from '../users.service';

@Component({
  selector: 'app-user-table',
  standalone: true,
  imports: [MatTableModule, CommonModule, MatToolbarModule, MatButtonModule, MatIconModule, MatDialogModule],
  templateUrl: './user-table.component.html',
  styleUrls: ['./user-table.component.css']
})
export class UserTableComponent implements OnInit {
  displayedColumns: string[] = ['id', 'username', 'name', 'bio', 'githubProfileUrl', 'skills', 'profileImageUrl', 'createdAt', 'updatedAt', 'actions'];
  dataSource: UserData[] = [];

  constructor(public dialog: MatDialog, private usersService: UsersService) { }

  ngOnInit(): void {
    this.loadUsers();
  }

  loadUsers(): void {
    this.usersService.getUsers().subscribe((users: UserData[]) => {
      this.dataSource = users;
    });
  }

  public addUser(userData: UserData | null = null): void {
    const dialogRef = this.dialog.open(UserFormComponent, {
      data: userData
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        if (result.id) {
          this.usersService.updateUser(result.id, result).subscribe(() => this.loadUsers());
        } else {
          this.usersService.createUser(result).subscribe(() => this.loadUsers());
        }
      }
    });
  }

  public editUser(userData: UserData): void {
    this.addUser(userData);
  }
}

