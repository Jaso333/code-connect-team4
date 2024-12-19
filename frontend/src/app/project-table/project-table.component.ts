import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProjectData, ProjectsService } from '../projects.service';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';
import { MatTableModule } from '@angular/material/table';
import { MatToolbarModule } from '@angular/material/toolbar';

@Component({
  selector: 'app-project-table',
  standalone: true,
  imports: [MatTableModule, CommonModule, MatToolbarModule, MatButtonModule, MatIconModule, MatDialogModule],
  templateUrl: './project-table.component.html',
  styleUrls: ['./project-table.component.css']
})
export class ProjectTableComponent {
  displayedColumns: string[] = ['id', 'name', 'description'];
  dataSource: ProjectData[] = [];

  constructor(private projectsService: ProjectsService) { }

  ngOnInit(): void {
    this.loadProjects();
  }

  loadProjects(): void {
    this.projectsService.getProjects().subscribe((projects: ProjectData[]) => {
      this.dataSource = projects;
    });
  }
}
