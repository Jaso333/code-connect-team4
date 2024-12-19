import { Component, Inject, Input, OnInit } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';

export interface UserData {
  id: number;
  username: string;
  name: string;
  bio: string;
  githubProfileUrl: string;
  skills: string;
  profileImageUrl: string;
  createdAt: Date;
  updatedAt: Date;
}

@Component({
  selector: 'app-user-form',
  standalone: true,
  imports: [ReactiveFormsModule, MatInputModule, MatButtonModule, MatCardModule],
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent implements OnInit {
  userForm: FormGroup;

  constructor(private fb: FormBuilder, @Inject(MAT_DIALOG_DATA) public userData: UserData | null = null, public dialogRef: MatDialogRef<UserFormComponent>) {
    this.userForm = this.fb.group({
      username: ['', Validators.required],
      name: ['', Validators.required],
      bio: [''],
      githubProfileUrl: ['', Validators.required],
      skills: [''],
      profileImageUrl: ['']
    });
  }

  ngOnInit(): void {
    if (this.userData) {
      this.userForm.patchValue(this.userData);
    }
  }

  onSubmit() {
    if (this.userForm.valid) {
      this.dialogRef.close(this.userForm.value);
    }
  }
}
