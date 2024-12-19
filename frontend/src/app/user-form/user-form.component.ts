import { Component, Input, OnInit } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';

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
  @Input() userData: UserData | null = null;
  userForm: FormGroup;

  constructor(private fb: FormBuilder) {
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
      console.log(this.userForm.value);
    }
  }
}
