class CabinsController < ApplicationController
  before_action :set_cabin, only: [:show, :edit, :update, :destroy]
  respond_to :html, :json

  def index
    @cabins = Cabin.all
    respond_with @cabins
  end

  def show
    respond_with @cabin
  end

  def new
    @cabin = Cabin.new
    respond_with @cabin
  end

  def edit
  end

  def create
    @cabin = Cabin.new(cabin_params)
    flash[:notice] = 'Cabin was successfully created. ' if @cabin.save
    respond_with @cabin
  end

  def update
    @cabin.update(cabin_params)
    respond_with @cabin
  end

  def destroy
    @cabin.destroy
    flash[:notice] = 'Cabin was successfully destroyed. '
    respond_with @cabin
  end

  private
    def set_cabin
      @cabin = Cabin.find(params[:id])
    end

    def cabin_params
      params.require(:cabin).permit(:navn, :address, :descritpion)
    end
end
