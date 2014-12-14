class UsersController < ApplicationController
  
  def show
  	if params[:id].nil?
    	@user = current_user
    else
  		@user = User.find(params[:id])
  	end
	@cabins = Cabin.all
  end

  def edit
  end

  def index
    redirect_to root_path
  end

end
