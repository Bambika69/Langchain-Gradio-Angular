import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { GoogleApiService } from '../google-api.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  userInfo: any;

  constructor(
    private userService: UserService,
    private googleApi: GoogleApiService) 
    {

    }

  ngOnInit() {
    this.userService.getUser().subscribe(user => {
      this.userInfo = user;
    });
  }

  logout() {
    this.googleApi.signOut();
  }
}
